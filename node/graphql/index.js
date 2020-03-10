const { ApolloServer } = require('apollo-server-express');

const typeDefs = require('./schema');
const resolvers = require('./resolvers');

const server = new ApolloServer({
  context: () => {
    return {
      user: {
        id: 1,
        username: 'Andres'
      }
    };
  },
  typeDefs,
  resolvers
});
module.exports = server;
