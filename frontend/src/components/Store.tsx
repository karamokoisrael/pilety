export default function Store(){
    return (
        <div>
                <div className="card lg:card-side bg-base-100 border mr-4 ">
            <div className='flex flex-col w-full lg:flex-row'>
                <div className="grid flex-grow h-32 p-4 font-extrabold font-size-50">Branch Name</div> 

                <div className="grid flex-grow h-32 ">
               
                        <div className="card-body">
                            <h2 className="card-title">Location Adress!</h2>
                            <p>Manager Phone number.</p>
                            <div className="card-actions justify-end">
                                <button className=" absolute top-0 right-0 rounded bg-white text-blue-700 btn">Edit</button>
                            </div>
                        </div>
                </div>

            
                </div>
            </div>    
        </div>

);
    

}