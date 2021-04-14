import { generalRequest, getRequest } from '../../utilities';
import { url, port, entryPoint } from './server';

const URL = `http://${url}:${port}/${entryPoint}`;

const resolvers = {
	Query: {
		allTransportes: (_) =>
			getRequest(URL, ''),
		transporteById: (_, { id }) =>
			generalRequest(`${URL}/${id}`, 'GET'),
	},
	Mutation: {
		createTransporte: (_, { transporte }) =>
			generalRequest(`${URL}/`, 'POST', transporte),
		updateTransporte: (_, { id, transporte }) =>
			generalRequest(`${URL}/${id}`, 'PUT', transporte),
		deleteTransporte: (_, { id }) =>
			generalRequest(`${URL}/${id}`, 'DELETE')
	}
};

export default resolvers;
