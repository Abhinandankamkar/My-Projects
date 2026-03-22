async function getWeather() {
  const city = document.getElementById("cityInput").value.trim();
  const apiKey = "cf6159098f9a058815ad60234beaa651"; // your key
  const weatherInfo = document.getElementById("weatherInfo");

  if (!city) {
    weatherInfo.innerHTML = "⚠️ Please enter a city name.";
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("City not found");
    const data = await response.json();

    weatherInfo.innerHTML = `
      <p>📍 <b>City:</b> ${data.name}</p>
      <p>🌡 <b>Temperature:</b> ${data.main.temp}°C</p>
      <p>☁ <b>Weather:</b> ${data.weather[0].description}</p>
      <p>💨 <b>Wind Speed:</b> ${data.wind.speed} m/s</p>
      <p>💧 <b>Humidity:</b> ${data.main.humidity}%</p>
    `;
  } catch (error) {
    weatherInfo.innerHTML = "❌ City not found or network issue.";
  }
}
