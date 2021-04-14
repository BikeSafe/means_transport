import merge from 'lodash.merge';
import GraphQLJSON from 'graphql-type-json';
import { makeExecutableSchema } from 'graphql-tools';

import { mergeSchemas } from './utilities';

import {
	transporteMutations, 
	transporteQueries,
	transporteTypeDef
} from './transport/transportes/typeDefs';

import transporteResolvers from './transport/transportes/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
	[
		'scalar JSON',
		transporteTypeDef
	],
	[
		transporteQueries
	],
	[
		transporteMutations
	]
);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
	typeDefs: mergedTypeDefs,
	resolvers: merge(
		{ JSON: GraphQLJSON }, // allows scalar JSON
		transporteResolvers
	)
});
