
import os

from flask import Flask, jsonify, render_template, request

import target

app = Flask(__name__)

# Only these functions can be called through the web interface.
AVAILABLE_FUNCTIONS = {
    "is_adult": target.is_adult,
    "celsius_to_fahrenheit": target.celsius_to_fahrenheit,
    "count_vowels": target.count_vowels,
    "invert": target.invert,
    "greet": target.greet,
    "find_max": target.find_max,
    "get_price": target.get_price,
    "swap": target.swap,
    "common_items": target.common_items,
    "is_leap_year": target.is_leap_year,
    "to_int": target.to_int,
    "divide": target.divide,
    "power": target.power,
    "square_root": target.square_root,
    "factorial": target.factorial,
    "average": target.average,
}


def convert_arguments(function_name, arguments):
    """Convert JSON values into the types expected by target.py."""

    converted = arguments.copy()

    if function_name == "swap" and isinstance(converted.get("pair"), list):
        converted["pair"] = tuple(converted["pair"])

    if function_name == "common_items":
        for key in ("set_a", "set_b"):
            if isinstance(converted.get(key), list):
                converted[key] = set(converted[key])

    return converted


def make_json_safe(value):
    """Convert Python values into JSON-compatible values."""

    if isinstance(value, (set, tuple)):
        return [make_json_safe(item) for item in value]

    if isinstance(value, list):
        return [make_json_safe(item) for item in value]

    if isinstance(value, dict):
        return {
            str(key): make_json_safe(item)
            for key, item in value.items()
        }

    return value


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/run", methods=["POST"])
def run_function():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "success": False,
                "error_type": "InvalidRequest",
                "error": "Please provide a valid JSON request."
            }), 400

        function_name = data.get("function")
        arguments = data.get("arguments", {})

        if function_name not in AVAILABLE_FUNCTIONS:
            return jsonify({
                "success": False,
                "error_type": "InvalidFunction",
                "error": "The selected function is not available."
            }), 400

        if not isinstance(arguments, dict):
            return jsonify({
                "success": False,
                "error_type": "InvalidArguments",
                "error": "Arguments must be provided as a JSON object."
            }), 400

        function_arguments = convert_arguments(
            function_name,
            arguments
        )

        result = AVAILABLE_FUNCTIONS[function_name](
            **function_arguments
        )

        return jsonify({
            "success": True,
            "function": function_name,
            "result": make_json_safe(result),
            "result_type": type(result).__name__
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error_type": type(error).__name__,
            "error": str(error)
        }), 400


@app.route("/health")
def health():
    commit_sha = (
        os.environ.get("RENDER_GIT_COMMIT")
        or os.environ.get("COMMIT_SHA")
        or os.environ.get("GITHUB_SHA")
        or "local-development"
    )

    return jsonify({
        "status": "healthy",
        "commit_sha": commit_sha
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
