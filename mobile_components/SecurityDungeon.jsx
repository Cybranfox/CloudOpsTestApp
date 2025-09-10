import React, { useState } from 'react';
import axios from 'axios';

export default function SecurityDungeon() {
  const [policy, setPolicy] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const resp = await axios.post('/api/minigame/security_dungeon', { policy });
    setResult(resp.data);
  };

  return (
    <div className="minigame-container">
      <h2>Security Dungeon</h2>
      <p>Fix the IAM policy to defeat the Vulnerability Goblins!</p>
      <form onSubmit={handleSubmit}>
        <textarea
          value={policy}
          onChange={(e) => setPolicy(e.target.value)}
          placeholder='{ "Version": "2012-10-17", "Statement": [...] }'
          rows={10}
          cols={40}
        />
        <button type="submit">Submit Policy</button>
      </form>
      {result && (
        <div className="result">
          {result.success ? <span className="success">✅</span> : <span className="error">❌</span>}
          {result.message}
        </div>
      )}
    </div>
  );
}
