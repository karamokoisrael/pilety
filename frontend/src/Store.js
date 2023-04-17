// import { configureStore, combineReducers } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import { configureStore, combineReducers } from '@reduxjs/toolkit';
import {productListReducer, productDetailsReducer} from './reducers/productReducers'
import {cargoListReducer, cargoDetailsReducer} from './reducers/cargoReducers'
import {cartReducer} from './reducers/cartReducers'

const rootReducer = combineReducers({
  // cargoList: cargoListReducer,
  // productList: productListReducer,
  // cargoDetails: cargoDetailsReducer,
  // productDetails: productDetailsReducer,
  // cart: cartReducer,
});
const cartItemsFromStorage = localStorage.getItem('cartItems') ?
    JSON.parse(localStorage.getItem('cartItems')) : []
 

const middleware = [thunkMiddleware];

const store = configureStore({
  reducer: rootReducer,
  middleware: middleware,
  devTools: process.env.NODE_ENV !== 'production' ? composeWithDevTools() : undefined,
});

export default store;


