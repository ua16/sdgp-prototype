<script>
    import Navbar from "../Navbar.svelte";

    import { onMount } from "svelte";

    let x = false;
    onMount(() => {
        x = localStorage.getItem("signedin") === "true";
    });

    function signInUser() {
        localStorage.setItem("signedin", "true");
    }
    function signOutUser() {
        localStorage.setItem("signedin", "false");
    }
</script>

<Navbar />
<div
    class="grid place-items-center h-screen bg-radial-[at_35%_25%] from-cyan-300 to-stone-100 to-90%"
>
    <div class="flex flex-col bg-stone-100 shadow-lg rounded-3xl p-4 md:p-50 gap-2">
        <button
            class="bg-cyan-300 hover:bg-cyan-400 text-black font-bold pl-20 pr-20 pt-10 pb-10 rounded-2xl"
            onclick={() => {
                signInUser();
            }}>Sign In (testing)</button
        >
        <button
            class="bg-cyan-300 hover:bg-cyan-400 text-black font-bold pl-20 pr-20 pt-10 pb-10 rounded-2xl"
            onclick={() => {
                signOutUser();
            }}>Sign Out (testing)</button
        >
    </div>
</div>
