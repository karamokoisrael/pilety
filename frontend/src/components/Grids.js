import React from 'react';
import './Grid.css'; // import CSS file with grid styles

function Grid() {
  const [gridSize, setGridSize] = React.useState(3); // default grid size of 3x3

  React.useEffect(() => {
    // update grid size based on device width
    const screenWidth = window.innerWidth;
    if (screenWidth < 640) { // small devices
      setGridSize(2);
    } else if (screenWidth < 1024) { // medium devices
      setGridSize(3);
    } else { // large devices
      setGridSize(4);
    }
  }, []);

  // create an array of cells based on grid size
  const cells = Array(gridSize ** 2).fill().map((_, i) => (
    <div className="cell" key={i}>{i + 1}</div>
  ));

  // set grid styles based on grid size
  const gridStyles = {
    gridTemplateColumns: `repeat(${gridSize}, 1fr)`,
    gridTemplateRows: `repeat(${gridSize}, 1fr)`,
  };

  return (
    <div className="grid" style={gridStyles}>
      {cells}
    </div>
  );
}

export default Grid;
