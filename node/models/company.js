'use strict';
module.exports = (sequelize, DataTypes) => {
  const Company = sequelize.define(
    'Company',
    {
      name: {
        type: DataTypes.STRING,
        allowNull: false
      }
    },
    {
      tableName: 'companies'
    }
  );
  Company.associate = function(models) {
    // associations can be defined here
  };
  return Company;
};
