import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        sand: {
          50: '#FCF8F3',
          100: '#F9F3EB',
          200: '#F3E5D3',
          300: '#ECD6BB',
          400: '#E5C8A3',
          500: '#DCB482',
          600: '#D4A164',
          700: '#C78738',
          800: '#A7712F',
          900: '#785121',
          950: '#543917',
        },
        storm: {
          50: '#F5F5F5',
          100: '#EBEBEB',
          200: '#D1D1D1',
          300: '#B5B5B5',
          400: '#949494',
          500: '#5E5E5E',
          600: '#545454',
          700: '#4A4A4A',
          800: '#383838',
          900: '#262626',
          950: '#1A1A1A',
        },
      },
    },
  },
  plugins: [],
}
export default config
