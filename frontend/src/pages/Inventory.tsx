import React from "react";
import PageWrapper from "../components/PageWrapper";
import ProductsList from "../components/Products";
import TopNavBar from "../components/navBar";
import OverallInventory from "../components/overallInventory";
import SideBar from "../components/sideBar";

export default function Inventory() {
  return (
    <PageWrapper>
      <>
        <div>
          <OverallInventory />
        </div>
        <div className="bg-base-200 rounded mt-4 mr-2">
          <ProductsList />
        </div>
      </>
    </PageWrapper>
  );
}
