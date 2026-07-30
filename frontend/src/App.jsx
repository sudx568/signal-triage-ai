import { useState } from "react";
import { motion } from "framer-motion";
import {
  Brain,
  Send,
  Activity,
  ShieldCheck,
  Clock,
  Sparkles
} from "lucide-react";


function App() {

  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);


  const analyzeSignal = async () => {

    if (!text.trim()) return;

    setLoading(true);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method:"POST",
          headers:{
            "Content-Type":"application/json"
          },
          body:JSON.stringify({
            text:text
          })
        }
      );


      const data = await response.json();


      setResult(data);


      setHistory([
        {
          message:text,
          category:data.category,
          confidence:data.confidence
        },
        ...history
      ]);


    } catch(error){

      console.log(error);

    }


    setLoading(false);

  };



  const confidence =
    result && typeof result.confidence === "number"
    ? Math.round(result.confidence * 100)
    : 0;



  return (

<div className="min-h-screen bg-slate-950 text-white p-8">


<div className="max-w-7xl mx-auto">



{/* HEADER */}

<div className="flex justify-between items-center mb-10">


<div className="flex items-center gap-4">

<div className="bg-blue-600 p-3 rounded-xl">

<Brain size={35}/>

</div>


<div>

<h1 className="text-4xl font-bold">

Jyot India

</h1>

<p className="text-slate-400">

Signal Intelligence Dashboard

</p>


</div>


</div>



<div className="bg-green-500/20 text-green-400 px-4 py-2 rounded-full">

🟢 AI Engine Online

</div>


</div>




{/* KPI CARDS */}


<div className="grid md:grid-cols-4 gap-5 mb-8">


<div className="bg-slate-900 p-5 rounded-2xl">

<Activity/>

<p className="text-slate-400 mt-3">
Total Signals
</p>

<h2 className="text-3xl font-bold">
128
</h2>

</div>



<div className="bg-slate-900 p-5 rounded-2xl">

<ShieldCheck/>

<p className="text-slate-400 mt-3">
AI Decisions
</p>

<h2 className="text-3xl font-bold">
115
</h2>

</div>



<div className="bg-slate-900 p-5 rounded-2xl">

<Clock/>

<p className="text-slate-400 mt-3">
Response Time
</p>

<h2 className="text-3xl font-bold">
0.8s
</h2>

</div>



<div className="bg-slate-900 p-5 rounded-2xl">

<Sparkles/>

<p className="text-slate-400 mt-3">
Accuracy
</p>

<h2 className="text-3xl font-bold">
86%
</h2>

</div>


</div>





{/* INPUT */}


<div className="bg-slate-900 rounded-3xl p-7">


<h2 className="text-2xl font-bold mb-4">

Analyze Customer Signal

</h2>


<textarea

className="w-full h-36 bg-slate-800 rounded-2xl p-5 outline-none"

placeholder="Enter customer issue..."

value={text}

onChange={(e)=>setText(e.target.value)}

/>



<button

onClick={analyzeSignal}

className="mt-5 flex items-center gap-3 bg-blue-600 px-8 py-3 rounded-xl hover:bg-blue-700"

>

<Send size={18}/>

{loading ? "Analyzing..." : "Analyze Signal"}

</button>


</div>






{/* RESULTS */}


{result &&

<motion.div

initial={{opacity:0,y:20}}

animate={{opacity:1,y:0}}

className="grid md:grid-cols-2 gap-6 mt-8"

>



<div className="bg-slate-900 p-7 rounded-3xl">


<h2 className="text-2xl font-bold">

AI Decision

</h2>



<div className="mt-5 space-y-3">


<p>

Category:

<span className="text-blue-400 ml-2">

{result.category}

</span>

</p>


<p>

Model:

<span className="ml-2">

{result.classifier}

</span>

</p>


<p>

Priority:

<span className="text-yellow-400 ml-2 uppercase">

{result.priority}

</span>

</p>


</div>



<p className="mt-6 text-green-400 font-semibold">

{result.action}

</p>


</div>






<div className="bg-slate-900 p-7 rounded-3xl">


<h2 className="text-2xl font-bold">

Confidence Score

</h2>



<h1 className="text-5xl font-bold mt-5">

{confidence}%

</h1>



<div className="bg-slate-700 h-4 rounded-full mt-5">


<div

className="bg-blue-500 h-4 rounded-full"

style={{
width:`${confidence}%`
}}

/>


</div>



</div>



</motion.div>

}






{/* HISTORY */}


<div className="bg-slate-900 rounded-3xl p-7 mt-8">


<h2 className="text-2xl font-bold mb-5">

Recent Signals

</h2>



{
history.map((item,index)=>(

<div

key={index}

className="border-b border-slate-700 py-4"

>


<p>
{item.message}
</p>


<p className="text-slate-400 text-sm mt-1">

{item.category} • {Math.round(item.confidence*100)}%

</p>


</div>


))
}



</div>




</div>


</div>

  );

}


export default App;