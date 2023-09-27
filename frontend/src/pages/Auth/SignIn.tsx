import Logo from '../../assets/logo-one.png';

export default function SignIn() {
  return (
    <div className="flex justify-center items-center h-screen bg-white ">
      <div className="p-8 rounded-lg w-96 ">
        <img className="mx-auto " src={Logo} alt="" />
        <h2 className=" text-2xl font-bold mb-1 text-black text-center">义乌市匹簕缇进出口有限公司</h2>
        <h2 className=" text-xs font-bold mb-4 text-black text-center">PILETY IMPORT AND EXPORT COMPANY LIMITED</h2>
        <p className="text-2xl mb-4 text-center"></p>
        <form className="bg-white">
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700 font-medium">
              Email Address
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-200 bg-white"
              placeholder="Enter your Email"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-700 font-medium">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              className="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-200 bg-white"
              placeholder="********"
              required
            />
          </div>
          <div className="mb-4">
            <label className="flex items-center">
              <input type="checkbox" className="form-checkbox" />
              <span className="ml-2 text-gray-600">Remember me</span>
            </label>
          </div>
          <button
            type="submit"
            className="w-full bg-blue-500 text-white font-medium py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200"
          >
            Sign In
          </button>
          <button
            type="submit"
            className="w-full text-blue font-medium py-2 rounded-lg mt-4 border border-blue-200 hover:bg-yellow-500 focus:outline-none focus:ring focus:ring-blue-200"
          >
            Sign In With Google
          </button>
        </form>
        <div className="mt-4 text-center">
          <a href="#" className="text-blue-500 hover:underline">
            Forgot your password?
          </a>
        </div>
      </div>
    </div>
  );
}
