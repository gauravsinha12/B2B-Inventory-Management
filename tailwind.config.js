/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './base/templates/**/*.html',
    './base/forms.py',
  ],
  variants:{
    extend:{
      display:["group-hover"],
    },
  },
  theme: {
    extend: {
      colors:{
        'orange-trans': '#D0B4AF',
        'green-trans': '#324343',
      }
    },
  },
  plugins: [],
}

