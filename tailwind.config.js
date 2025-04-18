/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./theme/templates/**/*.html",
		"./templates/*.html",
		"./theme/templates/*.html",
		"./static/css/src/*.css",
	],
  theme: {
		extend: {
			colors: {
					navy: '#000080',
					royal: '#4169e1',
			}
		},
  },
  plugins: [],
}

