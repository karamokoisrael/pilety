import ReportOverview from "../../components/BusinessAnalysis";
import BestSellingCartegory  from "../../components/BusinessAnalysis"
import BestSellingProducts  from "../../components/BusinessAnalysis"


export default function ReportsOverview(){
    return (
        <div className="mr-4">
            <div className="flex flex-col w-full border-opacity-50">
                <div className="grid card border">
                    <h1 className="m-4 text-xl "> Product Primary Details </h1>
                    
                    <div className="flex w-full ">
                        <div className="grid border flex-grow">

                            <ReportOverview/>
                            


                            
                        </div>
                        <div className="grid  border flex-grow place-items-center">
                            
                            
                        <BestSellingCartegory/>
                        
                        </div>
                    </div>
                </div>
                <div className="grid border mt-8">
                    <h1 className="text-xl"> Graphs </h1>
                    <div className="overflow-x-auto">
                        
                    </div>
                </div>
                <div className="grid border mt-8">
                    <h1 className="m-4 text-xl"> Top Selling Products </h1>
                    <BestSellingProducts/>
                </div>
            </div>
        </div>

    )
} 
