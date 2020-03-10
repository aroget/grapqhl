const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Company {
    id: ID!
    name: String!
    createdAt: String
    updatedAt: String
  }
  type Query {
    companies: [Company]
    companyById(id: ID!): Company
  }

  type Mutation {
    createCompany(name: String): Company
  }
`;

module.exports = typeDefs;
