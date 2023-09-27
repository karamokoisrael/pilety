
export default function NewProductsStore(){
    return (
        <div className="bg-white-300 rounded-lg w-96 items-right center align-right ">
            <h1 className=" text-3xl centered">Create a new Store</h1>

            <form className="form-control w-full max-w-xs">
                <div>
                    <label className="label">
                        <span className="label-text">Store Name</span>
                    </label>
                    <input type="text" placeholder="Enter Store Name" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Location</span>
                    </label>
                    <input type="text" placeholder=" Location" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Manager</span>
                    </label>
                    <input type="text" placeholder="Manager" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Manager's Phone number</span>
                    </label>
                    <input type="text" placeholder="+255123456789" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Status</span>
                    </label>
                    <input type="text" placeholder="Status" className="input input-bordered w-full max-w-xs" />
                </div>
                <div className="mt-8 join join-vertical lg:join-horizontal">
                    <button className="btn join-item  bg-blue-500 text-white font-medium py-2">Save</button>
                    <button className="btn join-item  bg-blue-500 text-white font-medium">Discard</button>

                
                </div>
            </form>
        </div>
    );
}