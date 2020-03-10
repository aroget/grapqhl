const { Sequelize } = require('sequelize');
const sequelize = new Sequelize(process.env.DATABASE_URI, {
  define: {
    timestamps: true,
    underscored: true
  }
});

module.exports = sequelize;
