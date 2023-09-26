import sideLogo  from '../assets/logo-one.png'
export default function SignUp(){
    return (
        <div className="bg-white h-screen flex gap-2 " >
            <div className="flex-initial w-1/2">
                <img className='justify-center' src={sideLogo} alt="My Image" />
            </div>
            <div className="bg-white-300 p-8 rounded-lg w-96 items-right center align-right flex-auto">
                <h2 className="text-3xl font-bold mb-4 text-black text-center">Welcome back! </h2>
                <p className="text-2xl mb-4 center" > Login to your account</p>
                <form className="bg-white-300">
                    <div className="mb-4">
                        <label htmlFor="username" className="block text-gray-700 font-medium">
                            Username
                            </label>
                        <input type="text" id="username" name="username" 
                            className="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-200 bg-white" 
                            placeholder="Enter your username" required/>

                        
                    </div>
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-gray-700 font-medium">
                            Email Address
                            </label>
                        <input type="email" id="email" name="email" 
                            className="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-200 bg-white" 
                            placeholder="Enter your Email" required/>

                        
                    </div>
                    <div className="mb-4">
                        <label  htmlFor="password" 
                                className="block text-gray-700 font-medium">Password</label>
                        <input type="password" id="password" name="password" 
                                className="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-200 bg-white" 
                                placeholder="Set a strong password" required/>
                    </div>
                    <div className="mb-4">
                        <label className="flex items-center">
                            <input type="checkbox" className="form-checkbox"/>
                            <span className="ml-2 text-gray-600">Remember me</span>
                        </label>
                    </div>
                    <button type="submit" 
                    className="w-full bg-blue-500 text-white font-medium py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200">
                        SignUp</button>
                    
                    <button type="submit" 
                    className="w-full bg-grey-500 text-blue font-medium py-2 rounded-lg mt-4 border border-blue-200 hover:bg-yellow-500 focus:outline-none focus:ring focus:ring-blue-200">
                        SignUp With Google</button>
                </form>
                <div className="mt-4 text-center">
                    <a href="#" className="text-blue-500 hover:underline">Forgot your password?</a>
                </div>
            </div>

        </div>
);
    

}