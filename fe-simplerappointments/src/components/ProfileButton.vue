<template>
  <div className="dropdown dropdown-end">
    <div tabIndex="{0}" role="button" className="btn btn-ghost btn-circle avatar">
      <div className="w-10 rounded-full">
        <img
          alt="Tailwind CSS Navbar component"
          src="data:image/jpeg;base64,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"
        />
      </div>
    </div>
    <ul
      tabIndex="{0}"
      className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
    >
      <li>
        <a href="/profile" className="justify-between">
          Profile
          <span className="badge">New</span>
        </a>
      </li>
      <li><a href="/settings">Settings</a></li>
      <li><a>Logout</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ProfileButton",
};
</script>
