import { Route, Routes, BrowserRouter as Router } from "react-router-dom";
import Home from "./pages/Home";
import Inventory from "./pages/Inventory/Inventory";
import ManageStore from "./pages/Stores/ManageStore";
import CreateNewStore from "./pages/Products/CreateNewStore";
import CreateNewProducts from "./pages/Products/CreateNewProduct";
import ProductsDetails from "./pages/Products/ProductsDetails";
import Reports from "./pages/Reports/Reports";
import FullContainersList from "./pages/Containers/FullContainersList";
import FullCargosList from "./pages/Cargos/FullCargosList";
import LooseContainersList from "./pages/Containers/LooseContainerList";
import LooseCargosList from "./pages/Cargos/LooseCargosList";
import StocksAvailable from "./pages/Stores/StocksAvailable";
import SignUp from "./pages/Auth/SignUp";
import SignIn from "./pages/Auth/SignIn";

export function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ac/api/login" element={<SignIn />} />
        <Route path="/ac/api/signup" element={<SignUp />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="fullcontainer/" element={<FullContainersList />} />
        <Route path="/fullcargo" element={<FullCargosList />} />
        <Route path="/loosecontainer" element={<LooseContainersList />} />
        <Route path="/loosecargo" element={<LooseCargosList />} />
        <Route path="/stocks" element={<StocksAvailable />} />
        <Route path="/warehouses" element={<ManageStore />} />
        <Route path="/product-details" element={<ProductsDetails />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/create-new-store" element={<CreateNewStore />} />
        <Route path="/create-new-product" element={<CreateNewProducts />} />
      </Routes>
    </Router>
  );
}

export default App;
