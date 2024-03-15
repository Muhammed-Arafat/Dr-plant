const citiesByCountry = {
USA: ['New York', 'Los Angeles', 'Chicago'],
Canada: ['Toronto', 'Vancouver', 'Montreal'],
Australia: ['Sydney', 'Melbourne', 'Brisbane'],
Iraq: ['bagdad', 'al_mousel', 'karkouk'],
};
// Get references to the country and city select elements
const countrySelect = document.getElementById('country-select');
const citySelect = document.getElementById('city-select');
// Add an event listener to the country select element to update the city options
countrySelect.addEventListener('change', () => {
// Get the selected country value
const country = countrySelect.value;
// Remove all existing city options
citySelect.innerHTML = '';
// If a country is selected, enable the city select element and add its cities as options
if (country) {
  citySelect.disabled = false;
  const cities = citiesByCountry[country];
  for (const city of cities) {
    const option = document.createElement('option');
    option.textContent = city;
    option.value = city;
    citySelect.appendChild(option);
  }
} else {
  // If no country is selected, disable the city select element
  citySelect.disabled = true;
  const option = document.createElement('option');
  option.textContent = 'Select a country first...';
  citySelect.appendChild(option);
}
});

// Add an event listener to the city select element to handle city selection
citySelect.addEventListener('change', () => {
// Get the selected city value
const city = citySelect.value;
console.log(`Selected city: ${city}`);
});
