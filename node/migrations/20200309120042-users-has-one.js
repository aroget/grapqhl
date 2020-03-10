'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {
    /*
      Add altering commands here.
      Return a promise to correctly handle asynchronicity.

      Example:
      return queryInterface.createTable('users', { id: Sequelize.INTEGER });
    */
    return queryInterface
      .addColumn('users', 'company_id', Sequelize.INTEGER, {
        after: 'password_hash'
      })
      .then(() =>
        queryInterface.addConstraint('users', ['company_id'], {
          type: 'foreign key',
          name: 'user_company_constraint',
          references: {
            table: 'companies',
            field: 'id'
          },
          onDelete: 'cascade',
          onUpdate: 'cascade'
        })
      );
  },

  down: (queryInterface, Sequelize) => {
    /*
      Add reverting commands here.
      Return a promise to correctly handle asynchronicity.

      Example:
      return queryInterface.dropTable('users');
    */

    return queryInterface
      .removeConstraint('users', 'user_company_constraint')
      .then(() => {
        return queryInterface.removeColumn('users', 'company_id');
      });
  }
};
