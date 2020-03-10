const db = require('../models');

module.exports = {
  Query: {
    companies: async () => {
      try {
        const companies = await db.Company.findAll();
        return companies;
      } catch (error) {
        return error;
      }
    },
    companyById: async (_, { id }, { user }) => {
      try {
        const company = await db.Company.findByPk(+id);
        return company;
      } catch (error) {
        return error;
      }
    }
  },
  Mutation: {
    async createCompany(_, { name }) {
      try {
        const newUser = await db.Company.create({ name });
        return newUser;
      } catch (error) {
        return error;
      }
    }
  }
};
