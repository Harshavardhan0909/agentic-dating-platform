"use client";

import { useEffect, useState } from "react";

type Persona = { id:string; name:string; vibe_summary:string; hobbies:string[]; intellectual_style:string; dealbreakers:string[]; avatar_url:string };
type Session = { transcript:{sender:string; dialogue:string; explanation:string}[]; overall_compatibility:number; chemistry_score:number; intellectual_score:number; lifestyle_score:number; match_analysis:string };
const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export default function Home() {
  const [personas,setPersonas] = useState<Persona[]>([]);
  const [selected,setSelected] = useState<Persona|null>(null);
  const [partner,setPartner] = useState<Persona|null>(null);
  const [session,setSession] = useState<Session|null>(null);
  const [rankings,setRankings] = useState<any[]>([]);
  const [loading,setLoading] = useState(false);
  useEffect(()=>{ fetch(`${API}/api/personas`).then(r=>r.json()).then((data)=>{setPersonas(data);setSelected(data[0]||null)}).catch(()=>{}); },[]);
  async function dateWith(p:Persona){ if(!selected)return; setPartner(p);setLoading(true);setSession(null); const r=await fetch(`${API}/api/date/simulate?person_a_id=${selected.id}&person_b_id=${p.id}`,{method:"POST"});setSession(await r.json());setLoading(false); }
  async function showRankings(){ if(!selected)return; const r=await fetch(`${API}/api/rankings/${selected.id}`);setRankings(await r.json()); }
  return <main className="shell"><header><div><span className="eyebrow">CONSENT-BASED AGENT LAB</span><h1>Cyrano<span>.ai</span></h1><p>Transparent profile analysis and simulated agent conversations.</p></div><div className="pill">{personas.length} demo profiles</div></header><section className="notice">Synthetic profiles only. Compatibility scores are illustrative and are not claims about real people.</section><div className="layout"><aside><h2>Agents</h2>{personas.map(p=><button className={selected?.id===p.id?"person active":"person"} onClick={()=>{setSelected(p);setSession(null);setRankings([])}} key={p.id}><img src={p.avatar_url}/><span>{p.name}<small>{p.vibe_summary}</small></span></button>)}</aside><section className="content">{selected&&<><div className="card hero"><img className="avatar" src={selected.avatar_url}/><div><h2>{selected.name}</h2><p>{selected.vibe_summary}</p><p><b>Style:</b> {selected.intellectual_style}</p></div></div><div className="grid"><article><h3>Hobbies</h3><ul>{selected.hobbies.map(x=><li key={x}>{x}</li>)}</ul></article><article><h3>Boundaries</h3><ul>{selected.dealbreakers.map(x=><li key={x}>{x}</li>)}</ul></article></div><div className="actions"><button onClick={showRankings}>View compatibility rankings</button>{personas.filter(p=>p.id!==selected.id).slice(0,3).map(p=><button className="secondary" key={p.id} onClick={()=>dateWith(p)}>Simulate date with {p.name}</button>)}</div></>}{loading&&<div className="card">Agents are simulating a respectful conversation…</div>}{session&&partner&&<div className="card"><h2>Date: {selected?.name} × {partner.name}</h2>{session.transcript.map((m,i)=><div className="message" key={i}><b>{m.sender}</b><p>{m.dialogue}</p><small>{m.explanation}</small></div>)}<div className="score">{session.overall_compatibility}% <small>illustrative compatibility</small></div><p>{session.match_analysis}</p></div>}{rankings.length>0&&<div className="card"><h2>Compatibility rankings</h2>{rankings.map((r,i)=><div className="rank" key={r.candidate_person_id}><b>#{i+1} {r.candidate_name}</b><strong>{r.score}%</strong><p>{r.compatibility_reason}</p><small>{r.friction_point}</small></div>)}</div>}</section></div></main>;
}
