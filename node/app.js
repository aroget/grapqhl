require('dotenv').config();

const express = require('express');

const server = require('./graphql');
const sequelize = require('./dastabase');

const app = express();
server.applyMiddleware({ app });

sequelize
  .authenticate()
  .then(() => console.log('DB connected'))
  .catch((e) => console.log('Error connnecting to DB', e));

app.listen({ port: 4000 }, () =>
  console.log(`🚀 Server ready at http://localhost:4000${server.graphqlPath}`)
);
