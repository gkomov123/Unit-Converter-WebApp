const conversions = {
  temperature: {
    "CtoF": "Celsius → Fahrenheit",
    "FtoC": "Fahrenheit → Celsius"
  },
  weight: {
    "kgToLb": "Kilogram → Pound",
    "lbToKg": "Pound → Kilogram"
  },
  length: {
    "mToFt": "Meter → Feet",
    "ftToM": "Feet → Meter",
    "mmtToCm": "Millimeter → Centimeter",
    "cmtToMm": "Centimeter → Millimeter"
  }
};

const categorySelect = document.getElementById("category");
const unitSelect = document.getElementById("unit");

categorySelect.addEventListener("change", function () {
    const selectedCategory = categorySelect.value;

    // clear old options
     unitSelect.innerHTML = "";

    // If no category selected, stop
    if (!selectedCategory) return;

    // Get all conversions for that category
    const categoryConversions = conversions[selectedCategory];

    // Loop through and create <option> for each
    for (const [key, label] of Object.entries(categoryConversions)) {
     const option = document.createElement("option");
     option.value = key;
     option.textContent = label;
     unitSelect.appendChild(option)
    }


});