import defaultTheme from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./hyacinth/templates/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans]
      },
      colors: {
        "hyacinth-primary": "#D5B9B2",
        "hyacinth-secondary": "#ECE2D0"
      }
    },
  },
  plugins: [],
}

