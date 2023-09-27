import PageWrapper from "../../components/PageWrapper";
import OverallInventory from "../../components/overallInventory";
import ProductsList from "../Products/Products";

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
