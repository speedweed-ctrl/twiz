import axios from 'axios';
import { IGetProductsResponse } from 'models';

const isProduction = true

export const getProducts = async () => {
  let response: IGetProductsResponse;

  if (isProduction) {
    response = await axios.get(
      'http://127.0.0.1:8000/api/products'
    );
  } else {
    response = require('static/json/products.json');
  }
  console.log(response.data)

  const { products } = response.data || [];

  return products;
};
