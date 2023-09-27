import { Link } from "react-router-dom";

export default function SideBar() {
        return (
          <div className="bg-White text-gray h-screen w-64 shadow-emerald-800 border-blue">
            {/* Sidebar Header */}
      
            {/* Sidebar Navigation */}
            <ul className="menu bg-base-200  rounded-box h-full">
            <Link className='mb-4 hover:text-red-300' to='/'><a>Home</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/inventory'><a>Inventory</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/warehouses'><a>Manage Stores</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/fullcontainer'><a>Full containers</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/fullcargo'><a>Full Cargos</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/loosecontainer'><a>Loose Containers</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/loosecargo'><a>Loose Cargo</a></Link>
            <Link className='mb-4 hover:text-red-300' to='/stocks'><a>Stocks</a></Link>
            
            </ul>
            
          </div>
        );
      
}