const configmapRootUrl = window._env_.CONFIGMAP_BACKEND_URL;
const rootUrl = configmapRootUrl ? configmapRootUrl : process.env.REACT_APP_BACKEND_URL;


export const fetchPostData = async (url, inputValue) => {
  url = rootUrl + url
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: inputValue }),
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  return response.json();
};


export const fetchPostHeaderData = async (url, inputValue) => {
  url = rootUrl + url
  const response = await fetch(url+"/"+inputValue, {method: "POST"});

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  return response.json();
};


export const fetchGetData = async (url) => {
  url = rootUrl + url
  console.log(url)
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  return response.json();
}


export const fetchDeleteData = async (url) => {
  url = rootUrl + url
  const response = await fetch(url, {method: "DELETE"});
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  return response.json();
}