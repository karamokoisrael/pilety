import { Route, Routes, BrowserRouter as Router} from "react-router-dom";
import Home from "./pages/Home";
import SignIn from "./pages/SignIn";
import Inventory from "./pages/Inventory";
import SignUp from "./pages/SignUp";
import ManageStore from "./pages/ManageStore";
import CreateNewStore from "./pages/CreateNewStore";
import CreateNewProducts from "./pages/CreateNewProduct";
import ProductsDetails from "./pages/ProductsDetails";
import Reports from "./pages/Reports";

export function App() {
      
      return (
        <Router>
      <Routes>
          <Route path="/" element={<Home />} exact/>
          <Route path="/ac/api/login" element={<SignIn />} />
          <Route path="/ac/api/signup" element={<SignUp />} />
          <Route path="/inventory" element={<Inventory />} />
          <Route path="/warehouses" element={<ManageStore />} />
          <Route path="/product-details" element={<ProductsDetails />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/create-new-store" element={<CreateNewStore />} />
          <Route path="/create-new-product" element={<CreateNewProducts />} />

      </Routes>
    </Router>
)}

export default App;
