import { Link } from "react-router-dom";

export default function SideBar() {
        return (
          <div className="bg-White text-gray h-full w-64 shadow-emerald-800 border-blue">
            {/* Sidebar Header */}
            <div className="p-4 text-2xl font-bold">....</div>
      
            {/* Sidebar Navigation */}
            <ul className="menu bg-base-200  rounded-box h-full">
            <Link className='mb-4 hover:text-red-300' to='/'><a>Home</a></Link>
            <Link className='mb-4 hover:text-red-300' to='inventory'><a>Inventory</a></Link>
            <Link className='mb-4 hover:text-red-300' to='warehouses'><a>Manage Stores</a></Link>
            <Link className='mb-4 hover:text-red-300' to='reports'><a>Reports</a></Link>
            
            </ul>
            
          </div>
        );
      
}