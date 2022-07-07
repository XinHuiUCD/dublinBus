export default {
  convertDegrees (from, to, value) {
    if (from === 'kelvin' && to === 'fahrenheit') {
      return (value - 273.15) * 9 / 5 + 32
    }
    if (from === 'kelvin' && to === 'celsius') {
      return value - 273.15
    }
    else {
      return value
    }
  },
  locationTitle (item) {
    if (item.countryCode === '') {
      return item.city
    }
    else {
      return [item.city, item.countryCode].join(', ')
    }
  }
}
