import axios from "axios";
import {CART_ADD_ITEM, CART_REMOVE_ITEM } from '../constants/cartConstants'


export const addToCart = (id, qty) => async (dispatch, getState) => {
    const {data } = await axios.get(`/api/merch_detail/${id}`)
    dispatch({
        type : CART_ADD_ITEM,
        payload : {
            product : data.id,
            name: data.name,
            image:data.images[0],
            price: data.price,
            stock: data.stock,
            qty
        }
    })
    localStorage.setItem('cartItems', JSON.stringify(getState().cart.cartItems))
}
