import TopNavBar from "./navBar";
import SideBar from "./sideBar";
import React from "react";
type Props = {
  children: React.ReactNode | React.ReactNode[];
};

export default function PageWrapper(props: Props) {
  return (
    <div>
      <TopNavBar />
      <div className="flex flex-col  lg:flex-row">
        <div
          className="grid flex-grow w-1/5 h-32 card bg-base-300 
                                rounded-box place-items-center mr-4"
        >
          <SideBar />
        </div>
        <div className="grid flex-grow h-32 card w-full">{props.children}</div>
      </div>
    </div>
  );
}
