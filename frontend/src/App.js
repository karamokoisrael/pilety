import { Container } from 'react-bootstrap'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

// componets
import Header from './components/Header'
import Footer from './components/Footer';

// screens
import HomePage from './screens/HomePage';
import ProductDetails from './screens/products_pages/ProductDetails';
import CartScreen from './screens/cart_pages/CartScreen';
// import Det from './screens/Det';


function App() {
  return (
    <Router>
      <Header/>
      
        <main className='py-3'>
          <Container>
            <Routes>
              <Route path='/' element={<HomePage/>}  exact />
              <Route path='/det/' element={<ProductDetails/>}  exact />
              {/* <Route path='/api/merch_detail/:id/' element={<ProductDetails/>}/>
              <Route path='cart/:id?' element={<CartScreen/>} /> */}
            </Routes>
          
          
          </Container>

        </main>
        
      <Footer />
    </Router>

  );
}

export default App;
