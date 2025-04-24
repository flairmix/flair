FROM node:23.11.0-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install --global vite
RUN npm install --verbose

COPY . .

EXPOSE 5173

# CMD ["npm", "run", "dev", '--', ""]