export const transporteTypeDef = `
  type Transporte { 
    id_transporte: Int!
    id_usuario: Int!  
    tipo_transporte: String!
    carac_transporte: String!
    color_transporte: String!
  }
  input TransporteInput {
    id_usuario: Int!  
    tipo_transporte: String!
    carac_transporte: String!
    color_transporte: String!
  }`;

export const transporteQueries = `
      allTransportes: [Transporte]!
      transporteById(id: Int!): Transporte!
  `;

export const transporteMutations = `
    createTransporte(transporte: TransporteInput!): Transporte!
    updateTransporte(id: Int!, transporte: TransporteInput!): Transporte!
    deleteTransporte(id: Int!): Int
`;
