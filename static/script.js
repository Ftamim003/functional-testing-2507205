
const functionDefinitions = {
    is_adult: {
        description: "Checks whether a person is 18 years old or above.",
        fields: [
            { name: "age", label: "Age", type: "json", placeholder: "e.g. 21", hint: "Enter a number." }
        ]
    },

    celsius_to_fahrenheit: {
        description: "Converts a Celsius temperature into Fahrenheit.",
        fields: [
            { name: "celsius", label: "Temperature in Celsius", type: "json", placeholder: "e.g. 37" }
        ]
    },

    count_vowels: {
        description: "Counts the vowels (a, e, i, o, u) in a text.",
        fields: [
            { name: "text", label: "Text", type: "string", placeholder: "Enter a sentence" }
        ]
    },

    invert: {
        description: "Returns the opposite value of a Boolean.",
        fields: [
            {
                name: "flag",
                label: "Boolean value",
                type: "select",
                options: [
                    { value: "true", label: "True" },
                    { value: "false", label: "False" }
                ]
            }
        ]
    },

    greet: {
        description: "Greets a person. If no name is provided, it uses Guest.",
        fields: [
            {
                name: "name",
                label: "Name (optional)",
                type: "string",
                placeholder: "Enter a name or leave empty",
                optional: true
            }
        ]
    },

    find_max: {
        description: "Finds the largest number in a list.",
        fields: [
            {
                name: "numbers",
                label: "Numbers",
                type: "json",
                placeholder: "[10, 20, 30]",
                hint: "Enter a JSON array, for example [10, 20, 30]."
            }
        ]
    },

    get_price: {
        description: "Finds the price of an item from a price dictionary.",
        fields: [
            {
                name: "prices",
                label: "Price dictionary",
                type: "json",
                placeholder: '{"apple": 50, "banana": 30}',
                hint: 'Example: {"apple": 50, "banana": 30}'
            },
            {
                name: "item",
                label: "Item name",
                type: "string",
                placeholder: "apple"
            }
        ]
    },

    swap: {
        description: "Reverses the order of a two-element pair.",
        fields: [
            {
                name: "pair",
                label: "Pair",
                type: "json",
                placeholder: '["first", "second"]',
                hint: "Enter exactly two elements in a JSON array."
            }
        ]
    },

    common_items: {
        description: "Finds the common elements between two sets.",
        fields: [
            {
                name: "set_a",
                label: "First set",
                type: "json",
                placeholder: "[1, 2, 3]",
                hint: "Enter a JSON array."
            },
            {
                name: "set_b",
                label: "Second set",
                type: "json",
                placeholder: "[2, 3, 4]",
                hint: "Enter a JSON array."
            }
        ]
    },

    is_leap_year: {
        description: "Checks whether a year is a leap year.",
        fields: [
            { name: "year", label: "Year", type: "json", placeholder: "e.g. 2024" }
        ]
    },

    to_int: {
        description: "Converts a value into an integer.",
        fields: [
            {
                name: "value",
                label: "Value",
                type: "json",
                placeholder: 'e.g. 25 or "25"',
                hint: 'Enter a JSON value, such as 25, "25", or true.'
            }
        ]
    },

    divide: {
        description: "Divides the first number by the second number.",
        fields: [
            { name: "a", label: "First number (a)", type: "json", placeholder: "e.g. 20" },
            { name: "b", label: "Second number (b)", type: "json", placeholder: "e.g. 4" }
        ]
    },

    power: {
        description: "Calculates a number raised to a given exponent.",
        fields: [
            { name: "base", label: "Base", type: "json", placeholder: "e.g. 2" },
            { name: "exponent", label: "Exponent", type: "json", placeholder: "e.g. 3" }
        ]
    },

    square_root: {
        description: "Calculates the square root of a number.",
        fields: [
            { name: "x", label: "Number", type: "json", placeholder: "e.g. 25" }
        ]
    },

    factorial: {
        description: "Calculates the factorial of a non-negative integer.",
        fields: [
            { name: "n", label: "Number", type: "json", placeholder: "e.g. 5" }
        ]
    },

    average: {
        description: "Calculates the average of a list of numbers.",
        fields: [
            {
                name: "numbers",
                label: "Numbers",
                type: "json",
                placeholder: "[10, 20, 30]",
                hint: "Enter a JSON array, for example [10, 20, 30]."
            }
        ]
    }
};

const functionSelect = document.getElementById("functionSelect");
const inputFields = document.getElementById("inputFields");
const functionForm = document.getElementById("functionForm");
const runButton = document.getElementById("runButton");
const healthStatusText = document.getElementById("healthStatusText");
const healthStatusDot = document.getElementById("healthStatusDot");
const deploymentHealth = document.getElementById("deploymentHealth");
const commitSha = document.getElementById("commitSha");

const emptyState = document.getElementById("emptyState");
const resultContent = document.getElementById("resultContent");
const resultStatus = document.getElementById("resultStatus");

const resultOutput = document.getElementById("resultOutput");
const resultType = document.getElementById("resultType");
const resultTypeSection = document.getElementById("resultTypeSection");

const errorSection = document.getElementById("errorSection");
const executedFunction = document.getElementById("executedFunction");

function renderInputFields() {
    const selectedFunction = functionSelect.value;
    const definition = functionDefinitions[selectedFunction];

    document.getElementById("functionDescription").textContent =
        definition.description;

    inputFields.innerHTML = "";

    definition.fields.forEach((field) => {
        const group = document.createElement("div");
        group.className = "field-group";

        const label = document.createElement("label");
        label.htmlFor = `field-${field.name}`;
        label.textContent = field.label;

        let input;

        if (field.type === "select") {
            input = document.createElement("select");

            field.options.forEach((option) => {
                const optionElement = document.createElement("option");
                optionElement.value = option.value;
                optionElement.textContent = option.label;
                input.appendChild(optionElement);
            });
        } else {
            input = document.createElement("input");
            input.type = "text";
            input.placeholder = field.placeholder || "";
            input.autocomplete = "off";
        }

        input.id = `field-${field.name}`;
        input.name = field.name;
        input.className = "input-field";

        if (!field.optional) {
            input.required = true;
        }

        group.appendChild(label);
        group.appendChild(input);

        if (field.hint) {
            const hint = document.createElement("small");
            hint.textContent = field.hint;
            group.appendChild(hint);
        }

        inputFields.appendChild(group);
    });

    clearResult();
}

function readArguments() {
    const selectedFunction = functionSelect.value;
    const definition = functionDefinitions[selectedFunction];
    const argumentsObject = {};

    for (const field of definition.fields) {
        const input = document.getElementById(`field-${field.name}`);
        const rawValue = input.value.trim();

        if (field.optional && rawValue === "") {
            continue;
        }

        if (field.type === "select") {
            argumentsObject[field.name] = rawValue === "true";
        } else if (field.type === "string") {
            argumentsObject[field.name] = input.value;
        } else {
            try {
                argumentsObject[field.name] = JSON.parse(rawValue);
            } catch {
                throw new Error(
                    `Invalid JSON in "${field.label}". Please enter a valid JSON value.`
                );
            }
        }
    }

    return argumentsObject;
}

function showResult(data) {
    emptyState.classList.add("hidden");
    resultContent.classList.remove("hidden");

    executedFunction.textContent = data.function || functionSelect.value;

    if (data.success) {
        resultStatus.textContent = "SUCCESS";
        resultStatus.className = "result-badge success";

        resultOutput.textContent = JSON.stringify(data.result, null, 2);

        resultType.textContent = data.result_type;
        resultTypeSection.classList.remove("hidden");
        errorSection.classList.add("hidden");
    } else {
        resultStatus.textContent = "ERROR";
        resultStatus.className = "result-badge error";

        resultOutput.textContent = "Function execution failed.";

        resultTypeSection.classList.add("hidden");
        errorSection.classList.remove("hidden");

        document.getElementById("errorType").textContent =
            data.error_type || "Error";

        document.getElementById("errorMessage").textContent =
            data.error || "An unexpected error occurred.";
    }

    document.getElementById("clearButton").classList.remove("hidden");
}

function clearResult() {
    emptyState.classList.remove("hidden");
    resultContent.classList.add("hidden");

    resultStatus.textContent = "WAITING";
    resultStatus.className = "result-badge idle";

    document.getElementById("clearButton").classList.add("hidden");
}

function setLoading(loading) {
    runButton.disabled = loading;
    runButton.innerHTML = loading
        ? "Running..."
        : "<span>▶</span> Run Function";
}

function showInputError(message) {
    showResult({
        success: false,
        function: functionSelect.value,
        error_type: "InputError",
        error: message
    });
}

functionForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    let argumentsObject;

    try {
        argumentsObject = readArguments();
    } catch (error) {
        showInputError(error.message);
        return;
    }

    setLoading(true);

    try {
        const response = await fetch("/api/run", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                function: functionSelect.value,
                arguments: argumentsObject
            })
        });

        const data = await response.json();
        showResult(data);

    } catch (error) {
        showInputError(
            "Could not connect to the server. Please check that Flask is running."
        );
    } finally {
        setLoading(false);
    }
});

functionSelect.addEventListener("change", renderInputFields);

document.getElementById("clearButton").addEventListener("click", clearResult);


// Display the initial function inputs.
renderInputFields();

// Retrieve application health and deployed commit information.
async function loadHealthStatus() {
    try {
        const response = await fetch("/health", {
            cache: "no-store"
        });

        if (!response.ok) {
            throw new Error("Health check failed.");
        }

        const data = await response.json();

        if (data.status !== "healthy") {
            throw new Error("Application is not healthy.");
        }

        // Update header status.
        healthStatusText.textContent = "Application Healthy";
        healthStatusDot.className = "status-dot healthy";

        // Update deployment information.
        deploymentHealth.textContent = "Healthy";
        deploymentHealth.className = "health-healthy";

        commitSha.textContent = data.commit_sha || "Not available";

    } catch (error) {
        healthStatusText.textContent = "Application Unavailable";
        healthStatusDot.className = "status-dot unavailable";

        deploymentHealth.textContent = "Unavailable";
        deploymentHealth.className = "health-unavailable";

        commitSha.textContent = "Unable to retrieve commit SHA";
    }
}

// Check application health when the page loads.
loadHealthStatus();