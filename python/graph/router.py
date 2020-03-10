from flask_graphql import GraphQLView
from graph.schema import schema


def router_init(app):
    app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
