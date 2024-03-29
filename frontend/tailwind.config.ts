import type { Config } from "tailwindcss";

export default <Partial<Config>>{
  theme: {
    fontFamily: {
      sans: ["Open sans", "sans-serif"],
      heading: ["Roboto", "sans-serif"]
    },
    extend: {
      colors: {
        text: {
          DEFAULT: "#050315",
          50: "#050316",
          100: "#0b062d",
          200: "#160d59",
          300: "#211386",
          400: "#2b19b3",
          500: "#3620df",
          600: "#5e4ce6",
          700: "#8779ec",
          800: "#afa6f2",
          900: "#d7d2f9",
          950: "#ebe9fc"
        },
        background: {
          DEFAULT: "#FAFAFA",
          50: "#0d0d0d",
          100: "#1a1a1a",
          200: "#333333",
          300: "#4d4d4d",
          400: "#666666",
          500: "#808080",
          600: "#999999",
          700: "#b3b3b3",
          800: "#cccccc",
          900: "#e6e6e6",
          950: "#f2f2f2"
        },
        primary: {
          DEFAULT: "#333333",
          50: "#0d0d0d",
          100: "#1a1a1a",
          200: "#333333",
          300: "#4d4d4d",
          400: "#666666",
          500: "#808080",
          600: "#999999",
          700: "#b3b3b3",
          800: "#cccccc",
          900: "#e6e6e6",
          950: "#f2f2f2"
        },
        secondary: {
          DEFAULT: "#00C853",
          50: "#001a0b",
          100: "#003315",
          200: "#00662b",
          300: "#009940",
          400: "#00cc55",
          500: "#00ff6a",
          600: "#33ff88",
          700: "#66ffa6",
          800: "#99ffc4",
          900: "#ccffe1",
          950: "#e5fff0"
        },
        accent: {
          DEFAULT: "#009688",
          50: "#001a17",
          100: "#00332e",
          200: "#00665c",
          300: "#00998a",
          400: "#00ccb8",
          500: "#00ffe6",
          600: "#33ffeb",
          700: "#66fff0",
          800: "#99fff5",
          900: "#ccfffa",
          950: "#e5fffc"
        }
      }
    }
  }
};
