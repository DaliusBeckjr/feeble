/** @type {import('tailwindcss').Config} */
// const colors = require('tailwindcss/colors')
const daisyui = require('daisyui')

export default {
  content: [ './src/**/*.{js,ts,jsx,tsx}',],
  theme: {
    extend: {
      colors: {
        // additional custom colors can be added here...
        watermelon: {
          50: "#FDEBF0",
          100: "#FAD1DD",
          200: "#F6A3BB",
          300: "#F17499",
          400: "#EC4678",
          500: "#E8476A", // base color
          600: "#C33C5D",
          700: "#9E314E",
          800: "#79263F",
          900: "#541B2F"
        },
        yaleBlue: {
          50: "#D3E1EB",
          100: "#A6C3D7",
          200: "#7AA5C3",
          300: "#4D87AF",
          400: "#21699B",
          500: "#083D77", // base Color
          600: "#063161",
          700: "#04244B",
          800: "#021735",
          900: "#010B1F",
        },

      },
    },
  },
  plugins: [
    daisyui,
  ],
}

