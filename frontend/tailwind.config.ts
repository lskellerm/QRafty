import type { Config } from 'tailwindcss';
import animate from 'tailwindcss-animate';

export default <Partial<Config>>{
  darkMode: ['class'],
  content: [
    './pages/**/*.{ts,tsx,vue}',
    './components/**/*.{ts,tsx,vue}',
    './app/**/*.{ts,tsx,vue}',
    './src/**/*.{ts,tsx,vue}'
  ],
  prefix: '',
  theme: {
    container: {
      center: true,
      padding: '2rem',
      screens: {
        '2xl': '1440px'
      }
    },
    fontFamily: {
      sans: ['Open sans', 'sans-serif'],
      heading: ['Poppins', 'sans-serif']
    },
    extend: {
      colors: {
        text: {
          DEFAULT: '#050315',
          50: '#050316',
          100: '#0b062d',
          200: '#160d59',
          300: '#211386',
          400: '#2b19b3',
          500: '#3620df',
          600: '#5e4ce6',
          700: '#8779ec',
          800: '#afa6f2',
          900: '#d7d2f9',
          950: '#ebe9fc'
        },
        backgroundColor: {
          DEFAULT: '#FAFAFA',
          50: '#0d0d0d',
          100: '#1a1a1a',
          200: '#333333',
          300: '#4d4d4d',
          400: '#666666',
          500: '#808080',
          600: '#999999',
          700: '#b3b3b3',
          800: '#cccccc',
          900: '#e6e6e6',
          950: '#f2f2f2'
        },
        primaryColor: {
          DEFAULT: '#333333',
          50: '#0d0d0d',
          100: '#1a1a1a',
          200: '#333333',
          300: '#4d4d4d',
          400: '#666666',
          500: '#808080',
          600: '#999999',
          700: '#b3b3b3',
          800: '#cccccc',
          900: '#e6e6e6',
          950: '#f2f2f2'
        },
        secondaryColor: {
          DEFAULT: '#00C853',
          50: '#001a0b',
          100: '#003315',
          200: '#00662b',
          300: '#009940',
          400: '#00cc55',
          500: '#00ff6a',
          600: '#33ff88',
          700: '#66ffa6',
          800: '#99ffc4',
          900: '#ccffe1',
          950: '#e5fff0'
        },
        accentColor: {
          DEFAULT: '#009688',
          50: '#001a17',
          100: '#00332e',
          200: '#00665c',
          300: '#00998a',
          400: '#00ccb8',
          500: '#00ffe6',
          600: '#33ffeb',
          700: '#66fff0',
          800: '#99fff5',
          900: '#ccfffa',
          950: '#e5fffc'
        }
      },
      keyframes: {
        'accordian-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' }
        },
        'accordian-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' }
        }
      },
      animation: {
        'accordian-down': 'accordian-down 0.3s ease-out',
        'accordian-up': 'accordian-up 0.3s ease-out'
      }
    }
  },
  plugins: [animate]
};
