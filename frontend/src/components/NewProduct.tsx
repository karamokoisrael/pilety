
export default function NewProduct(){
    return (
        <div className="bg-white-300 px-3 rounded-lg w-96 items-right center align-right ">
            <h1 className=" text-3xl centered">Create a new Product</h1>
            <form className="form-control w-full max-w-xs">
                <div>
                    <label className="label">
                        <span className="label-text">Product Name</span>
                    </label>
                    <input type="text" placeholder="Enter Product Name" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Category</span>
                    </label>
                    <input type="text" placeholder="Choose the Product category" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                    <span className="label-text">Buying Price</span>
                    </label>
                    <input type="text" placeholder="Price/ctn" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Quantity</span>
                    </label>
                    <input type="text" placeholder="Quantity in ctns" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Unit</span>
                    </label>
                    <input type="text" placeholder="Pcs/bags/rolls/dozens" className="input input-bordered w-full max-w-xs" />
                </div>
                <div>
                    <label className="label">
                        <span className="label-text">Thresh hold</span>
                    </label>
                    <input type="text" placeholder="Enter the minimun Value" className="input input-bordered w-full max-w-xs" />
                </div>
                <div className="mt-8 join join-vertical lg:join-horizontal">
                    <button className="btn join-item  bg-blue-500 text-white font-medium py-2">Save</button>
                    <button className="btn join-item  bg-blue-500 text-white font-medium">Discard</button>

                
                </div>
            </form>
        </div>
    );
}