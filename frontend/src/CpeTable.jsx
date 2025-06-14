import React, { useEffect, useState } from 'react';
import api from './api';
import ReferenceLinks from './ReferenceLinks';

function CpeTable() {
  const [cpes, setCpes] = useState([]);
  const [page, setPage] = useState(1);
  const [limit] = useState(15);
  const [total, setTotal] = useState(0);
  const [filters, setFilters] = useState({
    title: '',
    uri: '',
    deprecation_date: ''
  });
  const [searchActive, setSearchActive] = useState(false);

  const fetchData = async (isSearch = false, pageNum = 1) => {
    try {
      let query = '';

      if (isSearch) {
        query = `/cpes/search?page=${pageNum}&limit=${limit}`;
        if (filters.title) query += `&cpe_title=${encodeURIComponent(filters.title)}`;
        if (filters.uri) query += `&cpe_uri=${encodeURIComponent(filters.uri)}`;
        if (filters.deprecation_date) query += `&deprecation_date=${filters.deprecation_date}`;
      } else {
        query = `/cpes?page=${pageNum}&limit=${limit}`;
      }

      const res = await api.get(query);
      setCpes(res.data.data);
      setTotal(res.data.total || 0);
      setPage(pageNum);
      setSearchActive(isSearch);
    } catch (err) {
      console.error("Error fetching CPEs:", err);
      setCpes([]);
      setTotal(0);
      setPage(1);
      setSearchActive(false);
    }
  };

  useEffect(() => {
    fetchData(searchActive, page);
  }, [page]);

  const formatDate = (date) => {
    if (!date) return "N/A";
    const d = new Date(date);
    return d.toLocaleDateString();
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>CPE Data Viewer</h2>

      <div style={{ marginBottom: '15px' }}>
        <input
          type="text"
          placeholder="Filter by Title"
          value={filters.title}
          onChange={(e) => setFilters({ ...filters, title: e.target.value })}
          style={{ marginRight: '10px' }}
        />
        <input
          type="text"
          placeholder="Filter by URI"
          value={filters.uri}
          onChange={(e) => setFilters({ ...filters, uri: e.target.value })}
          style={{ marginRight: '10px' }}
        />
        <input
          type="date"
          value={filters.deprecation_date}
          onChange={(e) => setFilters({ ...filters, deprecation_date: e.target.value })}
          style={{ marginRight: '10px' }}
        />
        <button onClick={() => fetchData(true, 1)}>Search</button>
        <button
          onClick={() => {
            setFilters({ title: '', uri: '', deprecation_date: '' });
            fetchData(false, 1);
          }}
          style={{ marginLeft: '10px' }}
        >
          Reset
        </button>
      </div>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Title</th>
            <th>URI 22</th>
            <th>URI 23</th>
            <th>Deprecation 22</th>
            <th>Deprecation 23</th>
            <th>Reference Links</th>
          </tr>
        </thead>
        <tbody>
          {cpes.length > 0 ? (
            cpes.map((cpe, idx) => (
              <tr key={idx}>
                <td title={cpe.cpe_title}>{cpe.cpe_title?.slice(0, 40)}...</td>
                <td>{cpe.cpe_22_uri}</td>
                <td>{cpe.cpe_23_uri || 'N/A'}</td>
                <td>{formatDate(cpe.cpe_22_deprecation_date)}</td>
                <td>{formatDate(cpe.cpe_23_deprecation_date)}</td>
                <td><ReferenceLinks links={cpe.reference_links} /></td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6" style={{ textAlign: 'center', padding: '15px' }}>
                {total === 0 ? '📭 No Data Available' : '❌ No Results Found'}
              </td>
            </tr>
          )}
        </tbody>
      </table>

      <div style={{ marginTop: '15px' }}>
        <button disabled={page === 1} onClick={() => setPage(page - 1)}>Prev</button>
        <span> Page {page} </span>
        <button disabled={(page * limit) >= total} onClick={() => setPage(page + 1)}>Next</button>
      </div>
    </div>
  );
}

export default CpeTable;
