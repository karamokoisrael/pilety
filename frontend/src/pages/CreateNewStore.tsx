import NewProductsStore from "../components/NewProductsStore";
import TopNavBar from "../components/navBar";
import SideBar from "../components/sideBar";



export default function CreateNewStore(){
    return (<div>
        <TopNavBar/>
        <div className="flex flex-col  lg:flex-row">
            <div className="grid flex-grow w-1/5 h-32 card bg-base-300 
                            rounded-box place-items-center mr-4"><SideBar/></div> 

            {/* <div className="divider lg:divider-horizontal"></div>  */}

            <div className="grid flex-grow h-32 card w-full">
              <NewProductsStore/> 
            </div>
        </div>
        
        </div>
    )
}