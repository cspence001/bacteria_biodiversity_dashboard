//read in .json

function plots(id) {
    d3.json("samples.json").then((data) => {
        // var samples = data.samples.filter(d => d.id ===id)[0];
        // var samples_ids = samples.filter(d => d.id ===id)[0];
        console.log(data);
        // console.log(samples_ids);
    })
};