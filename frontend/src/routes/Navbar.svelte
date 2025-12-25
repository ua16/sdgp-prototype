<script lang="ts">
    import { scale } from 'svelte/transition';
    
    let clicked = $state(false);
    function onclick() {
        clicked = !clicked;
    }
</script>

<nav>
    <div class="fixed m-5">
        {#if !clicked}
            <button 
                in:scale={{ duration: 150, delay: 200 }}
                out:scale={{ duration: 150 }}
                class="bg-stone-50 rounded-2xl hover:bg-stone-100 transition-colors absolute top-0 left-0" 
                onclick={onclick}
                aria-label="Open menu"
            >
                <img 
                    class="max-w-12 m-1" 
                    src="/HamburgerMenu.svg?url" 
                    alt="Hamburger Menu Icon" 
                />
            </button>
        {/if}
        
        {#if clicked}
            <div 
                in:scale={{ duration: 200, delay: 150, start: 0.95 }}
                out:scale={{ duration: 200, start: 0.95 }}
                class="bg-stone-50 rounded-2xl p-6 min-w-48 absolute top-0 left-0 text-stone-900"
            >
                <div class="flex justify-between items-center mb-4">
                    <h2 class="text-xl font-bold">Menu</h2>
                    <button 
                        class="text-2xl leading-none hover:text-stone-600" 
                        onclick={onclick}
                        aria-label="Close menu"
                    >
                        ×
                    </button>
                </div>
                <ul class="flex flex-col gap-3">
                    <li>
                        <a 
                            href="/" 
                            class="block py-2 px-3 hover:bg-stone-300 rounded-lg transition-colors"
                        >
                            Home
                        </a>
                    </li>
                    <li>
                        <a 
                            href="/about" 
                            class="block py-2 px-3 hover:bg-stone-300 rounded-lg transition-colors"
                        >
                            About
                        </a>
                    </li>
                    <li>
                        <a 
                            href="/signup" 
                            class="block py-2 px-3 hover:bg-stone-300 rounded-lg transition-colors"
                        >
                            Sign Up
                        </a>
                    </li>
                </ul>
            </div>
        {/if}
    </div>
</nav>
