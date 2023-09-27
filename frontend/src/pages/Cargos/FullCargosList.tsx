import TopNavBar from "../../components/navBar";
import OverallInventory from "../../components/overallInventory";
import SideBar from "../../components/sideBar";
import ProductsList from "../Products/Products";


export default function FullCargosList(){
    return (<div>
        <TopNavBar/>
        <div className="flex flex-col  lg:flex-row">
            <div className="grid flex-grow w-1/5 h-32 card bg-base-300 
                            rounded-box place-items-center mr-4"><SideBar/></div> 

            {/* <div className="divider lg:divider-horizontal"></div>  */}

            <div className="grid flex-grow h-32 card w-full">
                <div><OverallInventory/></div>
                <div className="bg-base-200 rounded mt-4 mr-2"><ProductsList/></div>
            </div>
        </div>
        
        </div>
    )
}